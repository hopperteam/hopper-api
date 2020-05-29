package golang

import "time"

// A notification on Hopper
type Notification struct {
	Type           string   `json:"type"`
	Heading        string   `json:"heading"`
	Content        string   `json:"content"`
	TimestampField int64    `json:"timestamp"`
	IsDoneField    bool     `json:"isDone"`
	IsSilentField  bool     `json:"isSilent"`
	ActionsField   []Action `json:"actions"`
}

// Creates a default notification with the given parameters
func DefaultNotification(heading string, content string) *Notification {
	return &Notification{"default", heading, content, time.Now().Unix()*1000, false, false, make([]Action, 0)}
}

// Sets isDone
func (not *Notification) IsDone(val bool) *Notification {
	not.IsDoneField = val
	return not
}

// Sets isSilent
func (not *Notification) IsSilent(val bool) *Notification {
	not.IsSilentField = val
	return not
}

// Sets the notification's timestamp
func (not *Notification) Timestamp(val int64) *Notification {
	not.TimestampField = val
	return not
}

// Adds the action to the notification
func (not *Notification) Action(val *Action) *Notification {
	not.ActionsField = append(not.ActionsField, *val)
	return not
}

// Override all previous added actions with the given array
func (not *Notification) Actions(val []Action) *Notification {
	not.ActionsField = val
	return not
}

// An action on Hopper
type Action struct {
	Type            string `json:"type"`
	Text            string `json:"text"`
	Url             string `json:"url"`
	MarkAsDoneField bool   `json:"markAsDone"`
}

// Creates a an action of type submit
func SubmitAction(text string, url string) *Action {
	return &Action{"submit", text, url, false}
}

// Creates a an action of type text
func TextAction(text string, url string) *Action {
	return &Action{"text", text, url, false}
}

// Creates a an action of type redirect
func RedirectAction(text string, url string) *Action {
	return &Action{"redirect", text, url, false}
}

// Sets whether triggering the action marks the notification as done
func (action *Action) MarkAsDone(val bool) *Action {
	action.MarkAsDoneField = val
	return action
}
