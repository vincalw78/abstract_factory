from rada_factories import UkraineRadaFactory

simulation_config_file = 'Ukraine'


if __name__=="__main__":
    if simulation_config_file == 'Ukraine':
        UkraineRadaFactory()().run()
    else:
        print('Nothing')
