""" File:        example_cmd_line.py
    Author:      Nathan Robinson
    Contact:     nathan.m.robinson@gmail.com
    Date:        2013-02-16
    URL:         https://bitbucket.org/nathanrobinson/python-command-line-processor
    Description: An example of how to use cmd_line.py showing different types of
                 arguments.
    
    Copyright (c) Year 2013, Nathan Robinson <nathan.m.robinson@gmail.com>
    
    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
    SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
    IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import sys
from cmd_line import ArgProcessor, ArgDefinition, FlagDefinition,\
    range_validator, enum_validator, bool_validator, InputException

def print_citation_info(arg_processor):
    print "When citing this planner please use the following publication:"
    print "TBA"
    sys.exit(0)

def process_args():
    arg_processor = ArgProcessor()
    
    arg_processor.add_program_arg('-req_str_arg', #The arg string
        ArgDefinition('required_string_argument', #The variable of the arg
            True, #If the arg is required
            None, #The validator, if any
            None, #The args to the validator
            None, #The default value for non required args
            "A required string arg with no validator")) #A description
    
    arg_processor.add_program_arg('-req_float_arg',
        ArgDefinition('required_float_argument',
            True,
            range_validator,
            [float, 0, 1, False, "Error - invalid floating point argument: "],
            None,
            "An required float arg with a lower bound of 0, an upper bound of 1"))
    
    arg_processor.add_program_arg('-opt_int_arg',
        ArgDefinition('optional_integer_argument',
            False,
            range_validator,
            [int, 0, None, True, "Error - invalid integer argument: "],
            None,
            "An optional integer argument with a lower bound of 0 and no upper bound"))
    
    arg_processor.add_program_arg('-opt_bool_arg',
        ArgDefinition('optional_boolean_argument',
            False,
            bool_validator,
            ["Error - invalid opt_bool_arg setting: "],
            True,
            "An optional Boolean argument with True as a default value"))

    arg_processor.add_program_arg('-opt_enum_arg',
        ArgDefinition('optional_enumerated_argument',
            False,
            enum_validator,
            [['value1', 'value2', 'value3'], "Error - invalid opt_enum_arg value: "],
            'value4',
            "An optional enumerated argument with three values"))
    
    arg_processor.add_program_flag('--cite',
        FlagDefinition('cite',
            print_citation_info,
            "Display citation information"))
    
    try:
        arg_processor.parse_args()
        
        #Do any inter-argument value checking here, raising input exceptions in
        #case of error.
        
    except InputException as e:
        print e.message
        print "Use --help flag to display usage information."
        sys.exit(1)
    return arg_processor


if __name__ == '__main__':
    args = process_args()
    
    print "Supplied arguments:"
    print "required_string_argument:", args.required_string_argument
    print "required_float_argument:", args.required_float_argument
    print "optional_integer_argument:", args.optional_integer_argument
    print "optional_boolean_argument:", args.optional_boolean_argument
    print "optional_enumerated_argument:", args.optional_enumerated_argument

