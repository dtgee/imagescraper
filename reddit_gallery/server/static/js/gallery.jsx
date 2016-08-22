var React = require('react');
var jquery = require('jquery');
import show_image from './show_image.js';

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
    console.log(this.state.data);
    var imageNodes = this.state.data.map(function(image) {
      /* test = Object.assign({}, image.id, image.path, image.url); */
      /* console.log("path: " + image['path']); */
      return (
	<Image data={image['path']}>
	</Image>
      );
    });

    console.log("nodes: " + imageNodes);
    return (
      <div className="gallery">
        {imageNodes}
      </div>
    );
  }

}

/* export? */
class Image extends React.Component{

  constructor(props) {
    super(props);
    console.log("passed: " + this.props.data);
    console.log(typeof show_image);
  }

  render() {
    function requireAll(r) {
      r.keys().forEach(r); 
    }
    requireAll(require.context('../../output/full/', true, /\.(png|jpg|jpeg|gif)$/));

    var imgName = "/static/bundles/output/" + this.props.data;
    return (
      <div className="image">
        <img className="single-image" src={imgName} />
      </div>
    );
  }

}
