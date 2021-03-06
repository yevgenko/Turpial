# -*- coding: utf-8 -*-

# Module to handle i18n
#
# Author: Wil Alvarez (aka Satanas)
# Oct 09, 2011

import os
import logging
import gettext

log = logging.getLogger('Lang')
log.debug('Started')

# Initialize gettext
gettext_domain = 'turpial'
# localedir definition in development mode
if os.path.isdir(os.path.join(os.path.dirname(__file__), '..', 'i18n')):
    localedir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'i18n'))
    trans = gettext.install(gettext_domain, localedir)
    log.debug('LOCALEDIR: %s' % localedir)
else:
    trans = gettext.install(gettext_domain)

STRINGS = {
    'twitter': 'Twitter',
    'identica': 'Identi.ca',
    'welcome': _('Welcome to Turpial!'),
    'no_active_accounts': _('You have no active accounts. Please register your \
accounts and add some columns'),
    'no_registered_accounts': _('No registered accounts'),
    'about': _('About'),
    'preferences': _('Preferences'),
    'update_status': _('Update status'),
    'accounts': _('Accounts'),
    'add_account': _('Add account'),
    'columns': _('Columns'),
    'column': _("Column"),
    'create_account': _('Create Account'),
    'login': _('Login'),
    'add': _('Add'),
    'reply': _('Reply'),
    'quote': _('Quote'),
    '+retweet': _('+Retweet'),
    '-retweet': _('-Retweet'),
    '+fav': _('+Fav'),
    '-fav': _('-Fav'),
    'show_all': _('Show all'),
    'delete': _('Delete'),
    'tweet': _('Tweet'),
    'tweets': _('Tweets'),
    'new_tweet': _('New Tweet'),
    'new_tweets': _('New Tweets'),
    'dent': _('Dent'),
    'dents': _('Dents'),
    'new_dent': _('New Dent'),
    'new_dents': _('New Dents'),
    'posts': _('Posts'),
    'following': _('Following'),
    'followers': _('Followers'),
    'favorites': _('Favorites'),
    'exit': _('Exit'),
    'user': _('User'),
    'password': _('Password'),
    'user_and_password': _('User and password'),
    'protocol': _('Protocol'),
    'close': _('Close'),
    'signin': _('Sign In'),
    'save': _('Save'),
    'ok': _('Ok'),
    'cancel': _('Cancel'),
    'search': _('Search'),
    'public_timeline': _('Public Timeline'),
    'saving': _('Saving...'),
    'loading': _('Loading...'),
    'connecting': _('Connecting...'),
    'authenticating': _('Authenticating...'),
    'authorizing': _('Authorizing...'),
    'secure_auth': _('Secure Authentication'),
    'authorize_turpial': _('Autorize Turpial, copy the PIN in the \
text box below and click OK:'),
    'login_cancelled': _('Login cancelled by user'),
    'invalid_pin': _('You must write a valid PIN'),
    'delete_account_confirm': _("Do you really want to delete the account "),
    'delete_column_confirm': _("Do you really want to delete the column "),
    'fields_cant_be_empty': _("Fields can't be empty"),
    'from': _("from"),
    'in_reply_to': _("in reply to"),
    'people': _("people"),
    'person': _("person"),
    'retweeted_by': _("Retweeted by"),
    'no_column_yet': _("There are no available columns because I'm still logging in"),
    'whats_happening': _("What's happening?"),
    'retweeting': _("Retweeting..."),
    'unretweeting': _("Undoing retweet..."),
    'successfully_retweeted': _("Status successfully retweeted"),
    'retweet_successfully_undone': _("Retweet successfully undone"),
    'successfully_deleted': _("Status sucessfully deleted"),
    'adding_to_fav': _("Adding to favorites..."),
    'removing_from_fav': _("Removing from favorites..."),
    'deleting': _("Deleting..."),
    'short_urls': _("Short URLs"),
    'short': _("Short"),
    'upload_image': _("Upload image"),
    'image': _("Image"),
    'send_with': _("Send with:"),
    'select_account_to_post': _("Select accounts to post"),
    'you_must_write_something': _("Hey! You must write something to post"),
    'message_like_testament': _("That message looks like a testament!"),
    'updating_status': _("Updating status..."),
    'error_posting_to': _("Error posting to %s"),
    'manual_update': _("Manual Update"),
    'delete_column': _("Delete Column"),
    'in_progress': _("In progress..."),
    'logged_in': _("Logged In"),
    'turpial_follow': _("Turpial (Follow)"),
    'turpial_unfollow': _("Turpial (Unfollow)"),
    'you_are_now_following': _("You are now following @%s"),
    'you_are_no_longer_following': _("You are no longer following @%s"),
    'user_profile': _("User Profile"),
    'bio': _("Bio"),
    'location': _("Location"),
    'web': _("Web"),
    'message': _("Message"),
    'follow': _('Follow'),
    'unfollow': _('Unfollow'),
    'requested': _("Requested"),
    'mute': _("Mute"),
    'unmute': _("Unmute"),
    'block': _("Block"),
    'spam': _("Spam"),
    'reporting_as_spam': _("Reporting as spam"),
    'user_reported_spam_successfully': _("User reported as spam successfully"),
    'blocking_user': _("Blocking user..."),
    'user_blocked_successfully': _("User blocked successfully"),
    'this_is_you': _("This is you!"),
    'following_user': _('Following user...'),
    'unfollowing_user': _('Unfollowing user...'),
    'you_are_now_following': _("You are now following @%s"),
    'you_are_no_longer_following': _("You are no longer following @%s"),
    'muting_user': _('Muting user...'),
    'unmuting_user': _('Unmuting user...'),
    'user_muted_successfully': _('User muted successfully'),
    'user_unmuted_successfully': _('User unmuted successfully'),
    'add_friend': _('Add friend'),
    'load_friends': _('Load friends'),
    'loading_friends': _('Loading friends...'),
    'friends': _('friends'),
    'friend': _('friend'),
    'friends_loaded_successfully': _('Friends loaded successfully'),
    'shorting_urls': _('Shorting URLs...'),
    'direct_messages': _('Direct Messages'),
    'direct_message': _('Direct Message'),
    'select_user': _('Select user'),
    'send_message_to': _('Send message to'),
    'can_send_message_to_one_account': _("Wait! I just can send messages to \
one account at once"),
    'sending_message': _('Sending message...'),
    'direct_message_sent_successfully': _('Direct message sent successfully'),
    'turpial_image_viewer': _("Turpial Image Viewer"),
    'general': _('General'),
    'notifications': _('Notifications'),
    'services': _('Services'),
    'web_browser': _('Web Browser'),
    'filters': _('Filters'),
    'proxy': _('Proxy'),
    'advanced': _('Advanced'),
    'delete_all_images_in_cache': _('Delete all images in cache'),
    'restore_config_warning': _('This action will close Turpial and will \
delete your current config (you must start Turpial again). Do you want to \
continue?'),
    'view_my_profile': _('View my profile'),
    'search_profile_in': ('Search profile in'),
    'profiles': _('Profiles'),
    'enable_sounds': _('Enable sounds'),
}

class i18n:
    @staticmethod
    def get(key):
        try:
            return STRINGS[key]
        except KeyError:
            return key
