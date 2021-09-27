from .mixins import GetView



class Resume(GetView):
    template_name = 'resume/resume.html'


class AboutMe(GetView):
    template_name = 'resume/aboutMe.html'


class GitHubProjects(GetView):
    template_name = 'resume/gitHubProjects.html'