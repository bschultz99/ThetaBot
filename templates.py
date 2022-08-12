takedown_form = [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Name"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a status"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "In-House"
						},
						"value": "value-IH"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Townsman"
						},
						"value": "value-TM"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "New Member"
						},
						"value": "value-NM"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Membership"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please Enter Your Takedown Availability."
			},
			"accessory": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Monday Lunch"
						},
						"value": "value-ML"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Monday Dinner"
						},
						"value": "value-MD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday Lunch"
						},
						"value": "value-TL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday Dinner"
						},
						"value": "value-TD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday Lunch"
						},
						"value": "value-WL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday Dinner"
						},
						"value": "value-WD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday Lunch"
						},
						"value": "value-RL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday Dinner"
						},
						"value": "value-RD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday Lunch"
						},
						"value": "value-FL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday Dinner"
						},
						"value": "value-FD"
					}
				],
				"action_id": "takedowns-action"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit"
					},
					"value": "takedowns-submit",
					"action_id": "actionId-takedownsubmit"
				}
			]
		}
]


help_message = """Welcome to the takedown bot. These are the following features:
1. \help - Gives information on how the slack commands work.
2. \\takedownform - Update your takedown availability
"""