import datetime
import lifx

# Turns on slowly over 5 minutes
TURN_ON_PERIOD = 5 * 60


if __name__ == '__main__':
    print(f'Wake up script was run at {datetime.datetime.now()}')
    lifx.ramp_on(TURN_ON_PERIOD)
