import os
import random
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
# いいねをしているかどうかで既にリプを送っているか判定
# そのため手動ふぁぼは「#春から名大 よろしく」を避けること

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
  # ふぁぼ＆リプ
  try:
    # いいね処理
    api.create_favorite(id=tweet.id)

    # リプライ処理／いいねで既にリプを送っているか判定する
    reply_msg = f'@{ tweet.user.screen_name } ' + random.choice(msgs_1) + random.choice(msgs_2) + random.choice(msgs_3)
    api.update_status(reply_msg, in_reply_to_status_id=tweet.id)

    print('\n==================================\n')
    print(f'No.{count}\n')
    print(tweet.text)
    print('')
    print("Like:", tweet.favorite_count)
    print(tweet.created_at)
    print(">", reply_msg)
  except:
    print('\n==================================\n')
    print(f'No.{count}\n')
    print("いいね済みだよ！")


print('\n==================================\n')
print(f"target_tweetsの要素数(max: {get_count}): {len(target_tweets)}")
print(f"fav_tweetsの要素数(max: 25): {len(fav_tweets)}")
print('')