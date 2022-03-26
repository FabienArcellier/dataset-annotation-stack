Label Studio is a open source data labeling tool.

## Build and run the image

```bash
docker build -t labelstudio .
docker run -it -p 8080:8080 -v /label-studio/data labelstudio
```

## Resources

* [website](https://labelstud.io/)
* [github](https://github.com/heartexlabs/label-studio)
