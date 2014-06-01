from django.shortcuts import redirect, render
from django.contrib import messages

from volunteering.models import Volunteer


def importer(request):
    if request.method == 'POST':
        lines = request.POST['csv'].splitlines()

        created_count = 0
        updated_count = 0
        for line in lines:
            parts = [part.strip() for part in line.split(',')]
            external_id = parts[0]
            name = " ".join(parts[1:3])
            phone = parts[3]

            v, created = Volunteer.objects.get_or_create(external_id=external_id)
            v.name = name
            v.phone_number = phone
            v.save()
            if created:
                created_count += 1
            else:
                updated_count += 1
        messages.success(request, '%s volunteers created and %s updated.' %
                         (created_count, updated_count))
        return redirect('/admin/volunteering/volunteer/')
    else:
        return render(request, 'volunteering/import.html')
