# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ShadowIGUser(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isShadowIGUser = True
        super(ShadowIGUser, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        biography = 'biography'
        business_discovery = 'business_discovery'
        followers_count = 'followers_count'
        follows_count = 'follows_count'
        id = 'id'
        ig_id = 'ig_id'
        media_count = 'media_count'
        mentioned_comment = 'mentioned_comment'
        mentioned_media = 'mentioned_media'
        name = 'name'
        profile_picture_url = 'profile_picture_url'
        username = 'username'
        website = 'website'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGUser,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, pending=False):
        from facebook_business.adobjects.instagraminsightsresult import InstagramInsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
            'since': 'datetime',
            'until': 'datetime',
            'metric': 'list<metric_enum>',
            'period': 'list<period_enum>',
        }
        enums = {
            'metric_enum': InstagramInsightsResult.Metric.__dict__.values(),
            'period_enum': InstagramInsightsResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramInsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramInsightsResult, api=self._api),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_media(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.shadowigmedia import ShadowIGMedia
        param_types = {
            'media_type': 'string',
            'caption': 'string',
            'image_url': 'string',
            'children': 'list<unsigned int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/media',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGMedia,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ShadowIGMedia, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_media_publish(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.shadowigmedia import ShadowIGMedia
        param_types = {
            'creation_id': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/media_publish',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGMedia,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ShadowIGMedia, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'biography': 'string',
        'business_discovery': 'ShadowIGUser',
        'followers_count': 'int',
        'follows_count': 'int',
        'id': 'string',
        'ig_id': 'int',
        'media_count': 'int',
        'mentioned_comment': 'ShadowIGComment',
        'mentioned_media': 'ShadowIGMedia',
        'name': 'string',
        'profile_picture_url': 'string',
        'username': 'string',
        'website': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


