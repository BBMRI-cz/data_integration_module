package pkg

import (
	"strings"
	"testing"
)

func TestGetXMLFile(t *testing.T) {
	name := "Gladys"
	testName := "Gladys"
	if strings.Compare(name, testName) != 0 {
		t.Failed()
	}
}
