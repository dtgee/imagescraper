var Gallery = React.createClass({
	getInitialStateL function() {
		return {data: []};
	},
	retrieveImages: function() {
		var retrieveScriptPath = "../../server/retrieve.py";
		$.ajax({
			url: retrieveScriptPath, 
			dataType: 'json',
			cache: false,
			success: function(data) {
				this.setState({data: data});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(retrieveScriptPath, status, err.toString());
			}.bind(this)
		});
	},
	render: function() {
		return (
				<div className="gallery">
					<Image data={this.state.data}></Image>
				</div>
		);
	}
});

var Image = React.createClass({
	render: function() {
		var showImagePath = "show_image.js"
		return (
			<div className="image">
				<script type="text/javascript" src=showImagePath path="'" + {this.props.path} + "'">
				</script>
			</div>
		);
	}
});

ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.getElementById('example')
);
