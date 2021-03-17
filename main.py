import os
import random
import datetime
import tweepy

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# 仕様
# 検索ワード・RT除外・いいね数下限設定で適切なツイートのみ取得
# そのうち今日投稿されたもののみいいねとリプライ
# これはいいねが重複してエラーになるのを防ぐため
# ほんとはfavoritedで判定したいけど反映されないし...
# Herokuのスケジューラを23:30に設定してその日の投稿をできるだけ取得


limit = 25
get_count = limit * 3 # 数に余裕を持たせてツイートを取得
threshold = 0 # いいね数の閾値
msgs_1 = [
  "ウホｯ！",
  "ウホｯ！？",
  "ウホｯ！ウホｯ！",
  "ウホｯ！ウホｯｩ！",
  "ウホウホｯｩ！！",
]
msgs_2 = [
  "すごいンダホｯ！",
  "よく頑張ったンダホｯ！",
  "おめでとうなンだホｯ！",
  "よろしくなんだホｯ！",
  "嬉しいんだホｯ！",
  "合格おめでとうなんだホｯ！",
  "お疲れ様なンだホｯ！",
  "おつかれ様なンだホｯ！",
]
msgs_3 = [
  "ウホｯ",
  "ウｯホｯ",
  "ウホｯ！ウホｯ！",
  "ウホホゥ",
  "ウホ〜ゥ！",
  "ホホゥ！ウホホゥ！！",
  "ウホホホ〜〜〜ゥ！！",
  "ウホホホ〜〜ゥ！",
  "ウホホ〜ゥ！",
]

# ツイートを取得
all_tweets = tweepy.Cursor(api.search, q="#春から名大 よろしく", result_type="recent", count=get_count).items(get_count)

# 検索ワードとRT削除、ふぁぼ数下限設定で新歓系を除き新入生のみに絞る
target_tweets = [tweet for tweet in all_tweets if (list(tweet.text[:2]) != ['R', 'T'] and tweet.favorite_count > threshold)]
# ふぁぼの上限を設ける
if len(target_tweets) > limit:
  fav_tweets = target_tweets[:limit]
else:
  fav_tweets = target_tweets

count = 0
for tweet in fav_tweets:
  count += 1
  # 今日投稿されたものならふぁぼ＆リプ
  created_at = datetime.datetime.strptime(f"{tweet.created_at}".split()[0], '%Y-%m-%d').date()
  today = datetime.date.today()
  if created_at == today:
    # いいね処理
    api.create_favorite(id=tweet.id)

    # リプライ処理
    reply_msg = msgs_1.choice() + msgs_2.choice() + msgs_3.choice()
    api.update_status(reply_msg, in_reply_to_status_id=tweet.id)

    print('\n==================================\n')
    print(f'No.{count}\n')
    print(tweet.text)
    print('')
    print("Like:", tweet.favorite_count)
    print(tweet.created_at)
    print(">", reply_msg)
  else:
    print('\n==================================\n')
    print(f'No.{count}\n')
    print("投稿日が今日じゃないみたい")
    print('\n==================================\n')


print('\n==================================\n')
print(f"target_tweetsの要素数(max: {get_count}): {len(target_tweets)}")
print(f"fav_tweetsの要素数(max: 25): {len(fav_tweets)}")
print(f"countの要素数(fav_tweetsの中で今日投稿されたもの): {count}")
print('')