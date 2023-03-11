Families = { 'chalrey':
                {'sam': {'boxy','rosy'},
                 'nila':{'pepsi'}},
             'devi':
                 {'tommy': {'tony'},
                  'timmy': {'hamster'},
                  'tammy':{'hamster'}},
             'carlos':
                 {'diego':'cat', 'ferret':'fox'}
            }
for Parent, Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s)")
    print(f" {', and '.join([str(Child) for Child in [*Children]])}")