#!/usr/bin/env bash
set -e
# see also ".mailmap" for how email addresses and names are deduplicated
OUT="${1:-.}"
{
	cat <<-'EOH'
	# File @generated by scripts/docs/generate-authors.sh. DO NOT EDIT.
	# This file lists all contributors to the repository.
	# See scripts/docs/generate-authors.sh to make modifications.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > "$OUT/AUTHORS"
cat "$OUT/AUTHORS"
