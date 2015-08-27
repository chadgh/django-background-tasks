from background_task import background


@background
def test():
    print('done')
