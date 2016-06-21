#!/usr/bin/python

#Global declaration
#------------------------------------------------------------------------------------------

import sys,psycopg2
function_list=["submitjob","getjobstatus","getalljobid","getproblems"]

#------------------------------------------------------------------------------------------

#Function definations
#------------------------------------------------------------------------------------------
def submitjob(final_input,input_length):
    connection=None
    try:
        connection = psycopg2.connect("dbname='online-db' user='daya'")
        curs=connection.cursor()
        curs.execute("INSERT INTO job (jobtype,problemid,jobfilename) VALUES (%s,%s,%s)",(final_input[1],final_input[2],final_input[3]))

        if(curs.execute("SELECT jobid FROM job WHERE jobtype IS (jobtype) VALUES (%s)",(final_input[1])) == NULL):
            print "Yes NULL"

        connection.commit()

    except psycopg2.DatabaseError,e:

        if connection:
            connection.rollback()

        print 'Error %s' % e

    finally:
        if connection:
            connection.close()

def getjobstatus():
    print "In getjobstatus"

def getalljobId():
    print "In getalljbId"

def getproblems():
    print "In getproblems"

#------------------------------------------------------------------------------------------

while True:
    print "                            UI                       \n"
    print "Please enter one of the options and pass neccessary arguments ...\n\n",
    print "submitjob    <JobType> <Problem ID> <Job Data File>\n",
    print "getjobstatus <JobId>\n",
    print "getalljobId\n",
    print "getproblems\n",
    print "exit\n\n",
    print "$ ",

    input_line=raw_input()
    input_length=len(input_line)
    final_input=input_line.split()

    if final_input[0] == 'submitjob':
        submitjob(final_input,input_length)
    elif final_input[0] == 'getjobstatus':
        getjobstatus()
    elif final_input[0] == 'getalljobid':
        getalljobId()
    elif final_input[0] == 'getproblems':
        getproblems()
    else:
        exit()

#-------------------------------------------------------------------------------------------
