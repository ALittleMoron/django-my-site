from .mixins import GetView



class Resume(GetView):
    template_name = 'resume/resume.html'