__author__ = 'youngsoul'

import re
import CommandCallbacks


class RegExCommandParser:

    def __init__(self):
        self.command_patterns = []

    def add_to_command_pattern(self, command_reg_ex, event_name=None, callback=None):
        '''
        Add a regular expression used to parse a command string to determine
        if it is a valid command
        It is generally expected that the regular expression will contain
        groups - as the groups are returned from the process_command method.

        :param command_reg_ex: regular expression to apply to command string
        :param callback: used when execute_command flag is True. The callback
        is meant to operate on a found command
        :return: void
        '''
        p1 = re.compile(command_reg_ex)
        self.command_patterns.append({'command_pattern': p1, 'event_name': event_name, 'callback': callback})

    def process_command(self, command_string, execute_command=False):
        '''
        process the command string against the previously added command patterns.

        :param command_string: Normal string representing the command
        :param execute_command: True - if there is a callback then use it.  False
        then do not execute any callback
        :return: List of groups from the regular expression match or None if no
        matches are found.
        '''
        parsed_command = []
        for command_pattern_rec in self.command_patterns:
            match = command_pattern_rec['command_pattern'].search(command_string)
            if match:
                for group in match.groups():
                    parsed_command.append(group)
                if command_pattern_rec['event_name'] is not None:
                    parsed_command.append(command_pattern_rec['event_name'])
                else:
                    parsed_command.append('')

                if execute_command:
                    if command_pattern_rec['callback'] is not None:
                        command_pattern_rec['callback'](parsed_command)

        if len(parsed_command) == 0:
            return None
        else:
            return parsed_command


# Example usage
if __name__ == "__main__":
    cmd_parser = RegExCommandParser()

    cmd_parser.add_to_command_pattern("^(Alarm clock)\s+(set\s+alarm)\s+_TIME\s+([\w:\s]*)\.\s+_END_TIME", 'set_alarm', getattr(CommandCallbacks, 'cb1'))
    cmd_parser.add_to_command_pattern("^(Alarm clock)\s+(display)\s+(status)")
    cmd_parser.add_to_command_pattern("^(Alarm clock)\s+(display)\s+(wealth)")
    cmd_parser.add_to_command_pattern("^(Alarm clock)\s+(display)\s+(weather\s+forecast)")
    cmd_parser.add_to_command_pattern("^(Alarm clock)\s+(say)\s+(weather\s+forecast)", 'say_forecast', getattr(CommandCallbacks, 'cb2'))


    sendemailto_reg_ex = '((?:[A-Z][a-z]+)).*?(".*?").*?((?:[a-z][a-z]+)).*?((?:[a-z][a-z]+)).*?([+-]?\d*\.\d+)(?![-+0-9\.]).*?((?:[a-z][a-z]+)).*?(".*?")'
    cmd_parser.add_to_command_pattern(sendemailto_reg_ex, 'sendemailto', getattr(CommandCallbacks, 'sendemailto'))


    value_to_parse = "Alarm clock set alarm _TIME 7:00 AM. _END_TIME"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock set alarm _TIME 7:00 AM. _END_TIME"
    cmd = cmd_parser.process_command(value_to_parse,True)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock display status"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "open the pod door hal"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock display wealth"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock display well"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock display weather forecast"
    cmd = cmd_parser.process_command(value_to_parse)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"

    value_to_parse = "Alarm clock say weather forecast"
    cmd_parser.process_command(value_to_parse,True)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"


    value_to_parse = 'Whenever "my test string" goes above 3.1415298 sendemailto "me@me.com,you@you.com"'
    cmd = cmd_parser.process_command(value_to_parse,True)
    print "------------Start-----------------"
    print value_to_parse
    print cmd
    print "-----------End------------------"


