import xlrd
from ofxstatement.parser import StatementParser
from ofxstatement.plugin import Plugin
from ofxstatement.statement import Statement, StatementLine, generate_transaction_id


class SwedbankXlsPlugin(Plugin):

    def get_parser(self, filename):
        bank_id = self.settings.get('bank', 'SWEDSESS')
        account_id = self.settings.get('account')
        return SwedbankParser(filename, bank_id, account_id)


class SwedbankParser(StatementParser):
    statement = Statement(currency='SEK')

    def __init__(self, filename, bank_id, account_id):
        self.filename = filename
        self.statement.bank_id = bank_id
        self.statement.account_id = account_id
        self.sheet = None
        self.row_num = 0
        self.date_format = "%Y-%m-%d"

    def parse(self):
        with xlrd.open_workbook(self.filename) as book:
            self.sheet = book.sheet_by_index(0)
            return super().parse()

    def split_records(self):
        rows = self.sheet.get_rows()
        next(rows)  # title 
        next(rows)  # name of holder
        next(rows)  # statement date and transaction types
        next(rows)  # currency and date range
        next(rows)  # clearing number
        next(rows)  # account number
        next(rows)  # empty spacing
        next(rows)  # headers
        return rows

    def parse_record(self, row):
        self.row_num += 1
        line = StatementLine()
        line.date = self.parse_datetime(row[2].value) # Using "transaktionsdag" instead of "bokföringsdag"
        line.refnum = str(row[0])

        referens = bytes(row[4].value, "utf-8").decode("cp1252")
        line.payee = referens # Using "Referens" as payee

        beskrivning = bytes(row[5].value, "utf-8").decode("cp1252")
        if beskrivning != referens : # If the "Beskrivning" column is different from "Referens", then add that as a memo
            line.memo = bytes(row[5].value, "utf-8").decode("cp1252")

        line.amount = row[6].value
        line.trntype = self.get_type(line)
        line.id = generate_transaction_id(line)

        return line

    @staticmethod
    def get_type(line):
        if line.amount > 0:
            return 'CREDIT'
        elif line.amount < 0:
            return 'DEBIT'
        else:
            return 'OTHER'
