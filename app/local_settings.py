# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2017 Ircam
# Copyright (c) 2016-2017 Guillaume Pellerin
# Copyright (c) 2016-2017 Emilie Zawadzki

# This file is part of mezzanine-organization.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date
import ldap, logging
from django.core.urlresolvers import reverse_lazy
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

DEBUG = True if os.environ.get('DEBUG') == 'True' else False

if DEBUG:
    MODELTRANSLATION_DEBUG = True

DOMAIN = "www.ircam.fr/"

IRCAM_EMPLOYER = 1

ADMINS = (
    ('Guillaume Pellerin', 'guillaume.pellerin@ircam.fr'),
    ('David Palomares', 'd.palomares@libelium.com'),
)

# Make these unique, and don't share it with anybody.
SECRET_KEY = "j1qa@u$5ktqr^0_kwh@-j@*-80t$)ht!4-=ybz1xc%@3+r(r&tzefoih"
NEVERCACHE_KEY = "m)u^%r@uh#r3wu0&$=#$1ogx)uy4hv93^2lt%c3@xi=^gifoj8paozijdihazefd"

EMAIL_HOST = 'smtp.ircam.fr'
EMAIL_PORT = '25'
SERVER_EMAIL = 'no-reply-vertigo@ircam.fr'
DEFAULT_FROM_EMAIL = 'Vertigo@iuk.fraunhofer.de'
DEFAULT_TO_EMAIL = 'Vertigo@iuk.fraunhofer.de'
EMAIL_SUBJECT_PREFIX = "[VERTIGO]"

SITE_TITLE = 'VERTIGO'
SITE_TAGLINE = 'VERTIGO'

EVENT_DOMAIN = "//eve.ircam.fr"
EVENT_SHOP_URL = EVENT_DOMAIN+"/pub.php/event/%d/edit"
EVENT_PASS_URL = EVENT_DOMAIN+"/pub.php/pass/"
EVENT_CONFIRMATION_URL = EVENT_DOMAIN+"/pub.php/cart/done?transaction_id=%s"
