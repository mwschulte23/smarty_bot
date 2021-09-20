#### Smarty Bot

##### Description
A chatbot to query your database for quick answers for end-user

##### Quick Start
1. Clone repo
2. Start action server `rasa run actions` to start custom action server
3. In separate terminal `rasa shell` to chat


##### TODO for v0.1
* stand-up a postgres database + add single table
* write db adapter
* change existing custom action to execute a query

Once above is complete, move to v1.0
1. Taps into dbt model via metricql or similar
2. Define rasa entities & slots that tie to dbt/metricql
3. Add rasa nlu training data, custom actions, stories & domain data 