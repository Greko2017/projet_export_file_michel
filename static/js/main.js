$(function() {

	$('select[multiple].active.3col').multiselect({
	  columns: 3,
	  placeholder: 'Select headers',
	  search: true,
	  searchOptions: {
	      'default': 'Search Headers'
	  },
	  selectAll: true
	});

});