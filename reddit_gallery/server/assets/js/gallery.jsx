var React = require('react');
var jquery = require('jquery');

export default class Gallery extends React.Component{

  constructor() {
    super();
    this.componentDidMount = this.componentDidMount.bind(this);
    this.state = {
      data: []
    }
  }

  componentDidMount() {
    $.ajax({
      type: "get",
      url: "/grab_images",
      cache: false,
      success: function(data) {
        console.log("success");
        this.setState({
          data: data
	});
      }.bind(this),
      error: function(xhr, status, err) {
        console.warn(xhr.responseText);
        console.error("grab_images", status, err.toString());
      }.bind(this)
    });
  }

  render() {
    return (
        <div className="gallery">
	hi
          <Image paths="test"></Image>
        </div>
    );
  }

}

/* export? */
class Image extends React.Component{

  constructor(props) {
    super(props);
    console.log(this.props.paths);
  }

  render() {
    var showImagePath = "/assets/js/show_image.js";
    return (
      <div className="image">
        <script type="text/javascript" src={showImagePath} data-path={image}>
        </script>
      </div>
    );
  }

}
