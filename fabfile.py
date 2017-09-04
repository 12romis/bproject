import sys

from fabric.api import run, env, local, sudo, prefix, task, cd
from fabric.operations import put
from fabric.context_managers import shell_env

# run production deploy with command "fab prod deploy"
# run qa deploy with command "fab test deploy"

env.path = '~/apps/buddha/bproject'


def clean():
    with cd(env.path):
        run('find . -name "*.pyc" -exec rm -f {} \;')


def update():
    with cd(env.path):
        run('git pull origin {}'.format(env.branch))
        with prefix('source /opt/apps/gb/bin/activate'):
            with shell_env(DJANGO_CONFIGURATION='{}'.format(env.config)):
                run('pip install -r requirements.txt')
                run('python manage.py migrate')
                run('python manage.py collectstatic --noinput')

    # for logs permission fix
    with cd('{}/logs'.format(env.path)):
        sudo('chmod g+w,o+w -R .')


@task
def restart():
    sudo('supervisorctl restart {}'.format(env.app))


@task
def deploy():
    """ Update and restart """
    clean()
    update()
    restart()


@task
def deploy_static():
    push()
    with cd(env.path):
        run('git pull')
        with prefix('source /opt/apps/gb/bin/activate'):
            run('python manage.py collectstatic --noinput')


@task
def test():
    env.hosts = ['10.1.0.45']
    env.branch = 'develop'
    env.user = 'vgalkin'
    env.key_filename = ["/home/xgalv00/.ssh/gb.key", ]
    env.app = 'gb celery'
    env.config = 'QA'
    env.run_user = 'gb'
    env.run_group = 'cogniance'


@task
def update_test():
    with cd(env.path):
        # sudo('chown -R {}:{} .'.format(env.user, env.run_group))
        run('git checkout {}'.format(env.branch))
        run('git pull origin {}'.format(env.branch))
        run('find . -name "*.pyc" -exec rm -f {} \;')
        # with prefix('source /opt/apps/gb/bin/activate'):
        with shell_env(DJANGO_CONFIGURATION='{}'.format(env.config)):
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')
    # for logs permission fix
    with cd('{}/logs'.format(env.path)):
        sudo('chmod g+w,o+w -R .')
    sudo('service apache2 restart')


@task
def prod():
    env.branch = 'master'
    env.hosts = ['ubuntu@54.165.65.110']
    env.user = 'ubuntu'
    env.key_filename = ["../gbproduction.pem", ]
    # version for gunicorn
    # env.app = 'gunicorn celery'
    env.app = 'gb celery'
    env.config = 'Production'
