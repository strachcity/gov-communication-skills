# An organisation as the customer

Tests that drafts work for a business with a named contact, and handle a contact who may have left.

- **skill:** government-communication
- **task:** draft
- **channel:** email
- **service context:** an invented business licence, below

## Prompt

Draft the email asking a business for its insurance certificate. Our last email to the named contact bounced, and we've found a second email address on the application.

## Service context

```
Service: Scaffolding licence (invented)
Customer: a business. Messages go to the named contact on the application
Customer word for the case: licence application
Sender: Scaffolding Licences
Contact: Telephone: 0300 000 7777, Monday to Friday, 9am to 5pm
Insurance certificate: needed before a decision. Upload at https://www.gov.uk/scaffolding-licence-documents. Status: confirmed
Deadline: none set. Status: confirmed
```

## A correct response must

- greet the named contact by name, as a per-message value
- name the business in the first line, like "the licence application for ((organisation name))"
- use the descriptive facts as given, like the sender, contact details and upload address, without asking for their status
- use variant D of "We need something from you", because the context confirms there's no deadline
- flag that the bounced email may mean the named contact has left, and that whether the second address belongs to someone with authority to act is a decision for the service
- treat the named contact's name and email address as personal data

## A correct response must not

- write "your licence application" as if the named contact owns it, without flagging it
- invent a deadline or consequence
- say which email address failed in a way that reveals it to someone else
