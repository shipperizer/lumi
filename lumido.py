# Lumi Coding Challenge
# _____________________
#
# We have a set of tasks, each running at least daily, which are scheduled with a simplified cron. We want to find when each of them will next run.
#
# The scheduler config looks like this (the task names are arbitrary examples here):
#
# 30 1 /bin/run_me_daily
# 45 * /bin/run_me_hourly
# * * /bin/run_me_every_minute
# * 19 /bin/run_me_sixty_times
#
# The first field is the minutes past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means that it should run for all values of that field. In the above example run_me_daily has been set to run at 1:30am every day and run_me_hourly at 45 minutes past the hour every hour. The fields are whitespace separated and each entry is on a separate line.
#
# We want you to write a command line program that when fed this config to stdin and the current time in the format HH:MM as a command line argument, outputs the soonest time at which each of the commands will fire and whether it is today or tomorrow. When it should fire at the current time that is the time you should output, not the next one.
#
# Given the above examples as stdin input and the command-line argument 16:10 the output should be
#
# 1:30 tomorrow - /bin/run_me_daily
# 16:45 today - /bin/run_me_hourly
# 16:10 today - /bin/run_me_every_minute
# 19:00 today - /bin/run_me_sixty_times
#
# It is easiest for us to run/review code written in a high-level, object-oriented or functional programming language such as Java, Python, Ruby, Scala, Clojure etc. If you want to use something more esoteric then it is advisable to check first. We will want to run your tool, so please supply instructions for running it. Additionally, it must work on at least one of OS X and Linux (so we can run it on our dev boxes), ideally both.
#
# Please submit all code as attachments, not in the body of the email, as formatting is often lost or mangled. Please include any test code. If you want to attach multiple files please do so as an archive (e.g. zip, tar, git bundle, etc).

class Cronjob:
    def __init__(self, minutes='*', hours='*', bin='/bin/bash'):
        self.minutes = minutes
        self.hours = hours
        self.bin = bin
        self.execs = []
        self._execs()

    def next(self, time):
        _time = int(''.join(time.split(':')))
        next_exec = self._next(_time)
        m = next_exec[0] % 100
        h = (next_exec[0] - m) / 100
        print('{:02}:{:02} {} - {}'.format(int(h), int(m), next_exec[1], self.bin))

    def _next(self, time):
        if not self.execs:
            # if empty means it's * *
            return time, 'today'
        else:
            for i in self.execs:
                if time <= i:
                    return i, 'today'
            return self.execs[0], 'tomorrow'

    def _execs(self):
        if self.hours == '*' and self.minutes == '*':
            # if * * pointless creating all the samples
            return
        else:
            if self.hours == '*':
                for h in range(24):
                    self._handle_minutes(h*100)
            else:
                self._handle_minutes(int(self.hours)*100)

    def _handle_minutes(self, hs):
        if self.minutes == '*':
            for m in range(60):
                self.execs.append(int(hs) + m)
        else:
            self.execs.append(int(hs) + int(self.minutes))


def main():
    crons = []
    with open('conf') as f:
        for line in f.readlines():
            c = Cronjob(*line.split())
            crons.append(c)
    time = input('insert time in format HH:MM: ')
    for cron in crons:
        cron.next(time)

if __name__ == '__main__':
    main()
