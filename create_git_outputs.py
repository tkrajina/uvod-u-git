import re as mod_re
import os as mod_os

BLUE = '\\textcolor{{blue}}{{{0}}}'
BLACK = '\\textcolor{{black}}{{{0}}}'
RED = '\\textcolor{{red}}{{{0}}}'
GREEN = '\\textcolor{{green}}{{{0}}}'
GRAY = '\\textcolor{{gray}}{{{0}}}'
ORANGE = '\\textcolor{{orange}}{{{0}}}'

class GitOutputSyntaxRule:

    detection_regex = None
    line_rules = None

    def __init__(self, detection_regex, line_rules):
        self.detection_regex = detection_regex
        self.line_rules = line_rules

types = [
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+status.*',
            line_rules = [
                    ('^(#\t)(.*)$', (GRAY, BLUE)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+rebase.*',
            line_rules = [
                    ('^(CONFLICT.*)$', (RED)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+branch.*',
            line_rules = [
                    ('^(\s*\*.*)$', (BLUE)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+merge(?!t).*',
            line_rules = [
                    ('^([^\$].*?)(\+*)(\-*)$', (BLUE, GREEN, RED)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+cherry.*',
            line_rules = [
                    ('^([^\$].*?)(\+*)(\-*)$', (BLUE, GREEN, RED)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$\s+git\s+log.*',
            line_rules = [
                    ('^(commit.*)$', (BLUE)),
           ]
    ),
    GitOutputSyntaxRule(
            detection_regex = '\$.*',
            line_rules = [
                    ('^(\$\s+)(.*)$', (GRAY, BLUE)),
            ]
    ),
    GitOutputSyntaxRule(
            detection_regex = 'diff\s+\-\-git.*',
            line_rules = [
                    ('^(index.*)$', (ORANGE)),
                    ('^(@@.*)$', (ORANGE)),
                    ('^(\-.*)$', (RED)),
                    ('^(\+.*)$', (BLUE)),
                    ('^(diff.*)$', (BLACK)),
           ]
    ),
]

def to_latex_string(string):
    string = string.replace('\\', '\\textbackslash{}')
    string = string.replace(' ', '\\ ')
    string = string.replace('%', '\%')
    string = string.replace('^', '\\^')
    string = string.replace('$', '\\$')
    string = string.replace('#', '\\#')
    string = string.replace('_', '\\_')
    string = string.replace('\t', '\ \ \ \ \ \ \ \ ')
    string = string.replace('<', '$<$')
    string = string.replace('>', '$>$')

    return string

def unnest(list_or_tuple):
    if isinstance(list_or_tuple, list) or isinstance(list_or_tuple, tuple):
        result = []
        for item in list_or_tuple:
            result += unnest(item)
        return result
    else:
        return [list_or_tuple]

def process_groups_and_rules(groups, rules):
    result = ''

    #print 'groups:', groups
    #print 'rules:', rules

    for i in range(len(groups)):
        group = groups[i]
        rule = rules[i]

        #print 'group:', group
        #print 'rule:', rule

        result += rule.format(to_latex_string(group))

    return result

def execute_git_output_rules(string, type_rules):
    result = ''
    rules = [
        ('^(\$\s*)(.*)$', (GRAY, BLUE)),
        ('^(.*)$', (GRAY)),
    ]
    for rule in type_rules:
        rules.insert(0, rule)
    for line in string.split('\n'):
        found = False
        for item in rules:
            rule_regex = item[0]
            rule_template = item[1 :]
            if not found and mod_re.match(rule_regex, line):
                groups = mod_re.findall(rule_regex, line)
                assert len(groups) == 1
                assert len(groups) == len(rule_template)

                result += process_groups_and_rules(unnest(groups), unnest(rule_template)) + '\\\\\n'

                found = True
        if not found:
            raise Exception('No rule for line: {0}'.format(line))
	
    return result

def to_latex(string):
    for rule in types:
        if mod_re.match(rule.detection_regex, string):
            return """\\gitoutput{%
\\noindent%
\\texttt{%
""" + execute_git_output_rules(string, rule.line_rules)[: -3] + '}}'
    raise Exception('Unknown git output for {0}'.format(string))

if __name__ == '__main__':
    for file_name in mod_os.listdir('git_output'):
        if file_name.endswith('.txt'):
            with file('git_output/{0}'.format(file_name)) as f:
                content = f.read().strip()
            latex = to_latex(content)
            latex_file_name = file_name.replace('.txt', '.tex')
            with file('git_output/{0}'.format(latex_file_name), 'w') as f:
                f.write(latex)
            print latex_file_name, 'OK'


