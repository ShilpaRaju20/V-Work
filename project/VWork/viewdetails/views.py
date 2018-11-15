import json
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.db import connection
from approach.models import Approach
from contractor_reg.models import contractor_reg


def views(request):
    login_id = request.session['logid']
    cursor = connection.cursor()
    cursor.execute("select con_id, contractor_name, phno, mail_id, amt from contractor_reg_contractor_reg a inner join approach_approach b on a.id=b.con_id where b.cust_id='%s'"%(login_id,))
    results_rows = []
    columns = ('con_id', 'contractor_name', 'phno', 'mail_id', 'amt')
    # raw = cursor.dictfetchall()
    # raw = AltwordManager.dictfetchall2(self, cursor)
    # raw = cursor.fetchall()
    for row in cursor.fetchall():
        results_rows.append(dict(zip(columns, row)))
    jsonformater = json.dumps(results_rows)
    jsonString = '{"result":' + jsonformater + '}'
    print(jsonString)
    jsonObject = json.loads(jsonString)


    # return render('Admin/AuthorDetails.html', data=jsonObject)
    # viewobj = Approach.objects.filter(cust_id=login_id)
    # conobj = contractor_reg.objects.filter(id=viewobj.con_id)

    # return render(request, "viewdetails/views.html", {'data': jsonObject})
    return render(request, "viewdetails/views.html", {'data': jsonObject['result']})