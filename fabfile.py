from fabric.api import local


def makemigrations(app=''):
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py makemigrations {}".format(app))


def migrate(app=''):
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py migrate {}".format(app))


def createsuperuser():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py createsuperuser")


def bash():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') bash")


def shell():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py shell")


def dev():
    local("docker-compose run --rm --service-ports server")


def kill():
    local("docker kill $(docker ps -q)")
