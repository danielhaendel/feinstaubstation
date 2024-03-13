from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def inner_run(self, *args, **options):
        print("""
                    ______     _            __              __         __        __  _           
                   / ____/__  (_)___  _____/ /_____ ___  __/ /_  _____/ /_____ _/ /_(_)___  ____ 
                  / /_  / _ \/ / __ \/ ___/ __/ __ `/ / / / __ \/ ___/ __/ __ `/ __/ / __ \/ __ \
                 / __/ /  __/ / / / (__  ) /_/ /_/ / /_/ / /_/ (__  ) /_/ /_/ / /_/ / /_/ / / / /
                /_/    \___/_/_/ /_/____/\__/\__,_/\__,_/_.___/____/\__/\__,_/\__/_/\____/_/ /_/ 
            """)
        super().inner_run(*args, **options)
