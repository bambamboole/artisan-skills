// visual-serve exposes one local directory for visual mockup review.
// Build: go build -o ../bin/visual-serve visual-serve.go
// Use:   visual-serve [-host 127.0.0.1] [-port 8787] DIRECTORY
package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"net/http"
	"os"
	"path/filepath"
)

func main() {
	host := flag.String("host", "127.0.0.1", "host interface to bind")
	port := flag.Int("port", 8787, "TCP port; use 0 for an available port")
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage: %s [-host 127.0.0.1] [-port 8787] DIRECTORY\n", filepath.Base(os.Args[0]))
	}
	flag.Parse()

	if flag.NArg() != 1 {
		flag.Usage()
		os.Exit(2)
	}
	root, err := filepath.Abs(flag.Arg(0))
	if err != nil {
		log.Fatal(err)
	}
	info, err := os.Stat(root)
	if err != nil {
		log.Fatal(err)
	}
	if !info.IsDir() {
		log.Fatalf("not a directory: %s", root)
	}

	listener, err := net.Listen("tcp", fmt.Sprintf("%s:%d", *host, *port))
	if err != nil {
		log.Fatal(err)
	}
	defer listener.Close()

	address := listener.Addr().String()
	log.Printf("Serving %s at http://%s", root, address)
	if err := http.Serve(listener, http.FileServer(http.Dir(root))); err != nil {
		log.Fatal(err)
	}
}
