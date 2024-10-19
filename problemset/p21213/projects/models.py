from django.contrib.auth.models import User
from django.db import models, transaction


class Project(models.Model):
    name = models.CharField(max_length=100)


class ProjectMembership(models.Model):
    ROLE_GUEST = 'RG'
    ROLE_REPORTER = 'RR'
    ROLE_DEVELOPER = 'RD'
    ROLE_MASTER = 'RM'
    ROLE_OWNER = 'RO'

    ROLE_CHOICES = (
        (ROLE_GUEST, 'Guest'),
        (ROLE_REPORTER, 'Reporter'),
        (ROLE_DEVELOPER, 'Developer'),
        (ROLE_MASTER, 'Master'),
        (ROLE_OWNER, 'Owner'),

    )

    permissions = {
        ROLE_GUEST: ['create_new_issue', 'leave_comments', ],
        ROLE_REPORTER: ['create_new_issue', 'leave_comments', 'pull_project_code', 'assign_issues_and_merge_requests',
                     'see_a_list_of_merge_requests', ],
        ROLE_DEVELOPER: ['create_new_issue', 'leave_comments', 'pull_project_code', 'assign_issues_and_merge_requests',
                      'see_a_list_of_merge_requests', 'manage_merge_requests', 'create_new_branches', ],
        ROLE_MASTER: ['create_new_issue', 'leave_comments', 'pull_project_code', 'assign_issues_and_merge_requests',
                   'see_a_list_of_merge_requests', 'manage_merge_requests', 'create_new_branches',
                   'add_new_team_members', 'push_to_protected_branches', ],
        ROLE_OWNER: ['create_new_issue', 'leave_comments', 'pull_project_code', 'assign_issues_and_merge_requests',
                  'see_a_list_of_merge_requests', 'manage_merge_requests', 'create_new_branches',
                  'add_new_team_members', 'push_to_protected_branches', 'switch_visibility_level', 'remove_project', ],
    }

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=4, choices=ROLE_CHOICES, default=ROLE_GUEST, verbose_name='Role')
    is_current = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'project')

    def has_permission(self, action):
        if action in self.permissions[self.role]:
            return True
        else:
            return False
