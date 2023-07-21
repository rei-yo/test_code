FROM ruby:2.7

# 環境変数の設定。
ENV RAILS_ENV=production

#javascript関連のライブラリをインストール
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update -qq \
  && apt-get install -y nodejs yarn

# 作業ディレクトリ
WORKDIR /app 

COPY ./src /app

#ライブラリのインストール
RUN bundle config --local set path 'vendor/bundle' \
  && bundle install

#start.shをルートディレクトリへコピー
COPY start.sh /start.sh
#start.shに実行権限を渡す。change modeで権限変更
RUN chmod 744 /start.sh
#dockerを実行するコマンドを設定。
CMD ["sh", "/start.sh"]