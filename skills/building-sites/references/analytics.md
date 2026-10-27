# Google Analytics through the existing Firebase CLI

This is the reusable website measurement pattern selected for this workflow. Use it when Analytics is requested or already part of the site's approved configuration. The plugin itself performs no account creation or tracking.

## Inspect and select explicitly

Use the existing Firebase CLI and authenticated accounts. Check command help for the installed version. Select the intended account/project on scoped commands rather than changing a default used by another project:

```sh
firebase login:list
firebase projects:list --account '<email>' --json
firebase apps:list WEB --account '<email>' --project '<project-id>' --json
firebase apps:sdkconfig WEB '<app-id>' --account '<email>' --project '<project-id>' --json
```

Reuse the website's existing app and GA4 stream. If a new web app is authorized and actually missing, `firebase apps:create WEB` registers it; inspect help for required flags. Confirm the Firebase project is linked to the intended Analytics property. A registered app alone does not prove an active Analytics integration. Record the real returned measurement ID and property/app/stream mapping. Never copy example/customer IDs into a new business.

Firebase CLI credentials do not necessarily have Analytics Admin/reporting scopes. If retention, enhanced measurement or reporting requires console access, record what the owner must check; do not claim app registration configured those settings. Never log access/refresh tokens or commit service credentials. Public website measurement identifiers are configuration, not authentication secrets.

## Website integration

A small Google tag integration can use a Firebase-linked web stream without a Firebase SDK, Firebase Hosting or a backend. Preserve the site's chosen measurement/consent model. For the basic consent-first pattern, load no Google tag before acceptance, make Allow/Decline equally usable, and provide a persistent settings/withdrawal control. Define preference/cookie expiry and withdrawal behavior, including storage failures and existing tabs. Keep advertising purposes disabled unless separately authorized.

Choose useful minimal events. A mailto click is a contact-link click, not a sent enquiry or a completed conversion. Do not send email addresses, query text or form contents as Analytics event data. Record whether preview traffic shares a stream or is separated; do not silently inherit another site's choice.

Align the privacy notice and CSP with actual behavior. Static generators may inline a small script and a strict CSP may block it; keep it external or deliberately hash it. Do not weaken CSP broadly just to get measurement working.

## Evidence and handoff

Use type/build and focused consent tests, then inspect the deployed browser: before consent, after acceptance, after withdrawal, storage-write failure, expiry and relevant cross-tab behavior. Check actual network requests, cookies, CSP errors and provider Realtime receipt. Attribute user confirmation as user confirmation. Static tests, a tag ID or HTTP 200 do not establish that Google received events.

Keep the chosen account, Firebase project/app, GA property/stream/ID, events, consent model, known settings, verification and reporting link in the site's README. This per-site information never becomes plugin defaults.

References: [Firebase CLI](https://firebase.google.com/docs/cli), [Firebase project/Analytics management](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project), [Analytics for web](https://firebase.google.com/docs/analytics/web/get-started).
