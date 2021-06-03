story = {
    'statement': 'On your way to your grand mother\'s home, you encounter a wolf in the forest.',
    'choices': [
        {
            'key': 'a',
            'label': 'Run.',
            'statement': 'You ran away from the wolf.',
            'choices': [
                {
                    'key': 'a',
                    'label': 'Run towards the village to look for the villagers.',
                    'statement': 'You\'re running.',
                    'choices': [
                         {
                             'key': 'a',
                             'label': 'Give up.',
                             'statement': 'LOSE: You\'ve given up finding someone to help you, the wolf catched up and eaten you alive.',
                         },
                        {
                             'key': 'b',
                             'label': 'Continue running.',
                             'statement': 'WIN: You found a villager and got help.',
                         }
                    ]
                },
                {
                    'key': 'b',
                    'label': 'Run to your home to hide.',
                    'statement': 'You reached your home.',
                    'choices': [
                        {
                            'key': 'a',
                            'label': 'Tell your mother what\'s happening.',
                            'statement': 'WIN: You told what happened to your mother and got help from villagers.',
                        },
                        {
                            'key': 'b',
                            'label': 'Keep it to yourself.',
                            'statement': 'LOSE: The wolf followed you and killed the unknowing villagers including you and your mother.',
                        }
                    ]
                },
                {
                    'key': 'c',
                    'label': 'Run towards grand mother\'s house.',
                    'statement': 'You reached your grand mother\'s house.',
                    'choices': [
                        {
                            'key': 'a',
                            'label': 'Look for hunters nearby.',
                            'statement': 'WIN: You found a hunter and he killed wolf.',
                        },
                        {
                            'key': 'b',
                            'label': 'Hide together with your grand mother.',
                            'statement': 'LOSE: The wolf found and killed both of you.',
                        }
                    ]
                }
            ]
        },
        {
            'key': 'b',
            'label': 'Converse with the wolf.',
            'statement': 'You continue talking to the wolf.',
            'choices': [
                {
                    'key': 'a',
                    'label': 'Tell the wolf about sick grand mother.',
                    'statement': 'The wolf looks sadden and wants cheers you up by playing with him.',
                    'choices': [
                         {
                             'key': 'a',
                             'label': 'Say goodbye and go to your grand mother\'s house.',
                             'statement': 'WIN: You reached grand mother\'s house. The wolf followed you but chased away by a hunter.',
                         },
                        {
                             'key': 'b',
                             'label': 'Play with the wolf.',
                             'statement': 'LOSE: The wolf ate you instead.',
                         }
                    ]
                },
                {
                    'key': 'b',
                    'label': 'Play with the wolf.',
                    'statement': 'LOSE: The wolf ate you instead.',
                }
            ]
        },
    ]
}


def process(part: dict):
    '''
    Process the story recursively.

    Keyword arguments:
    part -- the part of story (dict)
    '''

    print(part['statement'])

    if not 'choices' in part:
        return

    valid_keys = []
    answer = ''

    for choice in part['choices']:
        valid_keys.append(choice['key'])
        print(f"[{choice['key']}] {choice['label']}")

    while not answer in valid_keys:
        answer = input('Choice: ')

    print('\n')

    # Get the next choice dictionary that matches key with the given answer
    next_part = next(
        (item for item in part['choices'] if item['key'] == answer),
        None
    )

    process(next_part)


process(story)
