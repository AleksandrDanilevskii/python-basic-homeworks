#!/usr/bin/env sh

echo Run prestart script

flask db upgrade

flask db-create-test-users