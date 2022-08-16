<div align="center">
  <p align="center">
    <img src="" alt="PHQ"/>
  </p>
  <p align="center">
    🤝
  </p>
</div>

# PHQ Text Notifier

Using Twilio & PredictHQ, this program to sends a text message with an area's top events of the day. 

Currently set to include the top 5 events in an area.

## To Run

Download the project to the destination of your deepest desires... 

```shell
git clone https://github.com/hhheath/phq-text-notifier.git
```

Create and start a virtual environment... 

**Note:** This step is not required if you plan to run this as a CRON job. Instead, the requirements will need to be installed for the system user that will be running the cron.

```shell
python -m venv .venv

source .venv/bin/activate
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
- [ ] use [Temporal](https://temporal.io) to spawn text message workflows on a schedule instead of relying on cron. 
  - this would enable the ability to "productize" this a bit more so you could send text messages to many different numbers rather than just one at a time.

If you have any ideas, please feel free to open an issue!

