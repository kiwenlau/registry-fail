#!/bin/bash

# 31 latest images for benchmark
imagelist=(axle-base sultans-bin haproxy cb-shell dnsutils node-metrics container-metrics ruby-base ipsec multilevel drupal jruby openjdk mono glassfish jenkins-slave quickstart-python exhibitor ubuntu-perl swagger-editor serf dnsmasq gocd-base gocd-agent drill ubuntu-perl-dev devmachine buildpack-runner gcc buildstep gocd-server)

# calculate fail rate for each image
for imagename in ${imagelist[*]};
do
	echo -e "$imagename: \c"
	cat output/$imagename.txt | grep Test | grep -c ""
done

