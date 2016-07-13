var Gallery = React.createClass({
	getInitialState: function() {
		return {data: []};
	},
	componentDidMount: function() {
		$.ajax({
			type: 'get',
			url: "../../server/retrieve.py",
			dataType: 'json',
			cache: false,
			success: function(data) {
				console.log("success");
				this.setState({data: data});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error("../../server/retrieve.py", status, err.toString());
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
				<script type="text/javascript" src={showImagePath} data-path={this.props.path}>
				</script>
			</div>
		);
	}
});

ReactDOM.render(
	<Gallery />,
  document.getElementById('app')
);
