user_form = [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Full Name"
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
							"text": "In-House 2"
						},
						"value": "value-IH2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 3"
						},
						"value": "value-IH3"
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
					"action_id": "actionId-usersubmit"
				}
			]
		}
	]

remove_user_form = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select User to Remove"
			},
			"accessory": {
				"type": "users_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"action_id": "users_select-action"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Remove"
					},
					"value": "takedowns-submit",
					"action_id": "actionId-removesubmit"
				}
			]
		}
	]

cleanup_settings_form = [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Clean Up"
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
							"text": "None"
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "2nd"
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3rd"
						},
						"value": "3"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Deck Requirement"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Can Townsman be captains?"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Yes"
						},
						"value": "True"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No"
						},
						"value": "False"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Minimum In-House Brothers"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Minimum People"
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
					"action_id": "actionId-cleanupsettingssubmit"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Remove"
					},
					"value": "takedowns-submit",
					"action_id": "actionId-cleanupsettingremove"
				}
			]
		}
]

admin_add_form = [
	{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a position for the admin"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a position"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Theta 1"
						},
						"value": "Theta-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Theta 3"
						},
						"value": "Theta-3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Developer"
						},
						"value": "Developer"
					}
				],
				"action_id": "static_select-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick a user to make admin"
			},
			"accessory": {
				"type": "users_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"action_id": "users_select-action"
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
					"value": "adminadd-submit",
					"action_id": "actionId-adminaddsubmit"
				}
			]
		}
]

help_message = """Welcome to the takedown bot. These are the following features:
1. /help - Gives information on how the slack commands work.
2. /userform - Fill this out to update your name, membership, and takedown availability.
3. /cleanupsettings - ADMIN - Change cleanups settings i.e. membership, minimum people, etc.
4. /removeuser - ADMIN - Remove a user from the user, cleanups, and takedown database.
5. /generate-cleanup-database - ADMIN - Generate the cleanup database by adding the cleanups and setting default values to 0.
6. /generate-cleanups - ADMIN - Generates the weekly cleanups.
7. /generate-takedowns - ADMIN - Generates the weekly takedowns.
8. /revert-takedowns - ADMIN - Reverts the weekly takedown generation.
9. /display-takedowns - Display the takedown database.
10. /display-cleanups - Display the cleanups database.
11. /admin-form - ADMIN - Add admins to the system.
"""