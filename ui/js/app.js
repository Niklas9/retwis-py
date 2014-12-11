App = Ember.Application.create({
  LOG_TRANSITIONS: true,
});

App.ApplicationAdapter = DS.RESTAdapter.extend({
  namespace: 'api/v1'
});

App.Router.map(function() {
  this.resource('tweets');
  this.route('myprofile');
  this.route('register');
});

/*DS.RESTAdapter.reopen({
  host: 'http://172.16.45.129:5000',
  namespace: 'api/v1'
});*/

App.Tweet = DS.Model.extend({
  text: DS.attr('string'),
  user: DS.attr('string'),
  createdAt: DS.attr('string', {
  	defaultValue: function() { return new Date(); }
  })
});


App.TweetsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('tweet');
  },
});

App.TweetsController = Ember.ObjectController.extend({
   actions: {
    save: function(txt) {
      var tweet = this.store.createRecord('tweet', {
        text: txt,
        user: 'BajsArne'
      });
      tweet.save();
    }
   } 
});

App.MyprofileRoute = Ember.Route.extend({
  setupController: function(controller) {
    controller.set('title', 'My profile');
  },
});

App.RegisterRoute = Ember.Route.extend({
  setupController: function(controller) {
    controller.set('title', 'Register');
  },
});
