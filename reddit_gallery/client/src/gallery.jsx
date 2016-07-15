import React from 'react';
import $ from 'jquery';

var Gallery = React.createClass({
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    $.ajax({
      type: "get",
      url: "retrieve.py",
      dataType: "json",
      cache: false,
      success: function(data) {
        console.log("success");
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.warn(xhr.responseText);
        console.error("retrieve.py", status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    return (
        <div className="gallery">
          <Image data={this.state.data} />
        </div>
    );
  }
});

var Image = React.createClass({
  render: function() {
    var showImagePath = "src/show_image.js"
    return (
      <div className="image">
        <script type="text/javascript" src={showImagePath} data-path={this.props.path}>
        </script>
      </div>
    );
  }
});
