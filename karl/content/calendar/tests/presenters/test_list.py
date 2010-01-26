# Copyright (C) 2008-2009 Open Society Institute
#               Thomas Moroz: tmoroz@sorosny.org
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License Version 2 as published
# by the Free Software Foundation.  You may not use, modify or distribute
# this program under any other version of the GNU General Public License.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import unittest
import sys
import datetime
import time
import calendar
from karl.content.calendar.tests.presenters.test_base import dummy_url_for
from karl.content.calendar.tests.presenters.test_base import DummyCatalogEvent


class ListViewPresenterTests(unittest.TestCase):
    def setUp(self):
        calendar.setfirstweekday(calendar.SUNDAY)

    def test_has_a_name_of_list(self):
        focus_at = datetime.datetime(2009, 8, 26)
        now_at   = datetime.datetime.now()

        presenter = self._makeOne(focus_at, now_at, dummy_url_for)
        self.assertEqual(presenter.name, 'list') 

    def test_has_a_feed_url(self):
        focus_at = datetime.datetime(2009, 8, 1) 
        now_at   = datetime.datetime.now()

        presenter = self._makeOne(focus_at, now_at, dummy_url_for)

        self.assert_(presenter.feed_url.startswith('http'))

    def test_title_is_month_name_and_year(self):
        focus_at = datetime.datetime(2009, 8, 26)
        now_at   = datetime.datetime.now()

        presenter = self._makeOne(focus_at, now_at, dummy_url_for)
        self.assertEqual(presenter.title, 'Upcoming Events')

    # helpers

    def _makeOne(self, *args, **kargs):
        from karl.content.calendar.presenters.list import ListViewPresenter
        return ListViewPresenter(*args, **kargs)

