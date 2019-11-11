from django.conf import settings
from django.core.management import BaseCommand
from oauth2client.service_account import ServiceAccountCredentials
import gspread

from anijung.models import Judge, Company, Case, Decision


class Command(BaseCommand):
    def handle(self, *args, **options):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        cred = ServiceAccountCredentials.from_json_keyfile_dict(settings.GDRIVE_KEY, scope)
        doc = gspread.authorize(cred)
        ws = doc.open_by_key('1d1iud_-bfXPuu-yDQwUZJ_FPT-qIRh7mnMDZghrUDis')

        decision_judge_map = {}
        judge_decision_map = {}
        map_sheet = ws.worksheet('판결-판사')
        for row in map_sheet.get_all_values()[1:]:
            print(row)
            decision_id = row[0]
            judge_id = row[1]
            decision_judge_map[decision_id] = judge_id
            judge_decision_map[judge_id] = decision_id

        judge_sheet = ws.worksheet('판사')
        for row in judge_sheet.get_all_values()[1:]:
            print(row)
            judge_id = row[0]
            name = row[3]

            if not name:
                continue

            company_name = row[1]
            position = row[2]

            if company_name or company_name != '-':
                c, _ = Company.objects.get_or_create(name=company_name)
            else:
                c = None

            j, _ = Judge.objects.get_or_create(id=judge_id)
            j.company = c
            j.name = name
            j.position = position
            j.save()

        case_sheet = ws.worksheet('사건')
        for row in case_sheet.get_all_values()[1:]:
            print(row)
            case_id = row[0]
            title = row[1]

            c, _ = Case.objects.get_or_create(id=case_id)
            c.title = title
            c.save()

        decision_sheet = ws.worksheet('판결')
        for row in decision_sheet.get_all_values()[1:]:
            print(row)
            decision_id = row[0]

            case_id = row[1]
            if not case_id:
                continue
            case = Case.objects.get(id=case_id)

            if decision_id not in decision_judge_map:
                continue

            judge_id = decision_judge_map[decision_id]
            judge = Judge.objects.get(id=judge_id)

            d, _ = Decision.objects.get_or_create(id=decision_id)
            d.case = case
            d.judge = judge
            d.no = row[2]
            d.court = row[3]
            d.place = row[4]
            d.round = row[5]
            d.result = row[6]
            d.source = row[7]
            d.save()
