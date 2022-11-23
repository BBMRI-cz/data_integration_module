package pkg

import (
	"bytes"
	"fmt"
	xj "github.com/basgys/goxml2json"
	"os"
)

func ReadXMLFile(fileName string) {
	data, _ := os.ReadFile(fileName)
	json, _ := xj.Convert(bytes.NewReader(data))
	fmt.Println(json)
}
