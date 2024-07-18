#!/usr/bin/env groovy

def call(String url, String ref, String subDir, String credentialsId = 'tonyaps') {
    dir(subDir) {
        deleteDir()
        checkout scm: [$class: 'GitSCM',
                       userRemoteConfigs: [[url: url,
                                            credentialsId: credentialsId]],
                       extensions: [[$class: 'CloneOption',
                                     noTags: true,
                                     shallow: true,  
                                     timeout: 60]],
                       branches: [[name: ref]]],
                      poll: false
    }
}