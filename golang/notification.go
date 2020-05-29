package golang

import "time"

type Notification struct {
	Type           string   `json:"type"`
	Heading        string   `json:"heading"`
	Content        string   `json:"content"`
	TimestampField int64    `json:"timestamp"`
	IsDoneField    bool     `json:"isDone"`
	IsSilentField  bool     `json:"isSilent"`
	ActionsField   []Action `json:"actions"`
}

func DefaultNotification(heading string, content string) *Notification {
	return &Notification{"default", heading, content, time.Now().Unix()*1000, false, false, make([]Action, 0)}
}

func (not *Notification) IsDone(val bool) *Notification {
	not.IsDoneField = val
	return not
}

func (not *Notification) IsSilent(val bool) *Notification {
	not.IsSilentField = val
	return not
}

func (not *Notification) Timestamp(val int64) *Notification {
	not.TimestampField = val
	return not
}

func (not *Notification) Action(val *Action) *Notification {
	not.ActionsField = append(not.ActionsField, *val)
	return not
}

func (not *Notification) Actions(val []Action) *Notification {
	not.ActionsField = val
	return not
}

type Action struct {
	Type            string `json:"type"`
	Text            string `json:"text"`
	Url             string `json:"url"`
	MarkAsDoneField bool   `json:"markAsDone"`
}

func SubmitAction(text string, url string) *Action {
	return &Action{"submit", text, url, false}
}

func TextAction(text string, url string) *Action {
	return &Action{"text", text, url, false}
}

func RedirectAction(text string, url string) *Action {
	return &Action{"redirect", text, url, false}
}

func (action *Action) MarkAsDone(val bool) *Action {
	action.MarkAsDoneField = val
	return action
}
