from models import Section


def sections_list(request):
    text = Section.objects.all()
    return {'sections': text}
