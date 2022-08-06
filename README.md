# PHQ Text Notifier

Using Twilio & PredictHQ, this program to sends a text message with an area's top events of the day. 

Currently set to include the top 5 events in an area.

## To Run

Download the project to the destination of your deepest desires... 

```shell
git clone https://github.com/hhheath/phq-text-notifier.git
```

Install requirements...

```shell
pip install -r requirements.txt
```

Create `.env` file from example env...

```shell
cp .example.env .env
```

Then fill out the fields in the `.env` file. Where `POI` takes the following form (see the [PredictHQ Docs](https://docs.predicthq.com/resources/events) for more on `within`): 

```shell
<radius><unit>@lat,long
```

After requirement installation, it's really up to you on how you want to run it. The preferred method is to run a [cron job](https://www.hostinger.com/tutorials/cron-job). In this example, I've cloned the project into my home directory `~/`.

Add the following to your crontab (this runs the script every day at 9am)...

```shell
0 0 9 ? * * * python ~/phq-text-notifier/main.py
```

## Future Improvements

- [ ] offer other ways to send messages instead of just SMS

If you have any ideas, please feel free to open an issue! 
