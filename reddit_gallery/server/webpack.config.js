//Require our dependencies
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    //Base directory (absolute path) for resolving the entry option
    context: __dirname,
    //You don't have to specify the extension now,
    //Because you will specify extensions later in the `resolve` section
    entry: './assets/js/entry', 
    
    output: {
        //Where you want your compiled bundle to be stored
        path: path.resolve('./assets/bundles/'), 
        //Naming convention webpack should use for your files
        filename: '[name]-[hash].js', 
    },
    
    plugins: [
        //Tells webpack where to store data about your bundles.
        new BundleTracker({filename: './webpack-stats.json'}), 
        //Makes jQuery available in every module
        new webpack.ProvidePlugin({ 
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery' 
        })
    ],
    
    module: {
        loaders: [
            //A regex that tells webpack use the following loaders on all 
            //.js and .jsx files
            {
							 test: /\.jsx?$/, 
                //We definitely don't want babel to transpile all the files in 
                //node_modules. That would take a long time.
               exclude: /node_modules/, 
                //Use the babel loader 
               loader: 'babel-loader', 
               query: {
                    //Specify that we will be dealing with React code
                    presets: ['es2015', 'react'] 
                }
            },
						//Allow us to use url-loader to output images
						{
							 test: /\.(jpg|jpeg|png|gif)$/,
							 loader: 'url?limit=8192'
							 //loader: 'file?name=[path][name].[ext]'
							 //include: './output/full/'
						}
        ]
    },
    
    resolve: {
        //Tells webpack where to look for modules
        modulesDirectories: ['node_modules'],
        //Extensions that should be used to resolve modules
        extensions: ['', '.js', '.jsx'] 
    }   
}
